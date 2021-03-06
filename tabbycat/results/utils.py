from itertools import combinations

from django.db.models import Count
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from draw.models import Debate
from tournaments.utils import get_side_name


def set_float_or_int(number, step_value):
    """Used to ensure the values sent through to the frontend <input> are
    either Ints or Floats such that the validation can handle them properly"""
    if step_value.is_integer():
        return int(number)
    else:
        return number


def get_result_status_stats(round):
    """Returns a dict where keys are result statuses of debates; values are the
    number of debates in the round with that status.

    There is also an additional key 'B' that denotes those with ballots checked
    in, but whose results are not entered."""

    # query looks like: [{'result_status': 'C', 'result_status__count': 8}, ...]
    query = round.debate_set.values('result_status').annotate(Count('result_status')).order_by()

    # The query doesn't return zeroes where appropriate - for statuses with no
    # debates, it just omits the item altogether. So initialize a dict:
    choices = [code for code, name in Debate.STATUS_CHOICES]
    stats = dict.fromkeys(choices, 0)
    for item in query:
        stats[item['result_status']] = item['result_status__count']

    # separately, count ballot-in debates and subtract from the 'None' count
    ballot_in = round.debate_set.filter(result_status=Debate.STATUS_NONE, ballot_in=True).count()
    stats['B'] = ballot_in
    stats[Debate.STATUS_NONE] -= ballot_in

    return stats


def populate_identical_ballotsub_lists(ballotsubs):
    """Sets an attribute `identical_ballotsub_versions` on each BallotSubmission
    in `ballotsubs` to a list of version numbers of the other BallotSubmissions
    that are identical to it.

    Two ballot submissions are identical if they share the same debate, motion,
    speakers and all speaker scores."""

    from .prefetch import populate_results
    populate_results(ballotsubs)

    for ballotsub in ballotsubs:
        ballotsub.identical_ballotsub_versions = []

    for ballotsub1, ballotsub2 in combinations(ballotsubs, 2):
        if ballotsub1.result.identical(ballotsub2.result):
            ballotsub1.identical_ballotsub_versions.append(ballotsub2.version)
            ballotsub2.identical_ballotsub_versions.append(ballotsub1.version)

    for ballotsub in ballotsubs:
        ballotsub.identical_ballotsub_versions.sort()


def ballot_checkin_number_left(round):
    return Debate.objects.filter(round=round, ballot_in=False).count()


_ORDINALS = {
    1: ugettext_lazy("1st"),
    2: ugettext_lazy("2nd"),
    3: ugettext_lazy("3rd"),
    4: ugettext_lazy("4th"),
    5: ugettext_lazy("5th"),
    6: ugettext_lazy("6th"),
    7: ugettext_lazy("7th"),
    8: ugettext_lazy("8th"),
}


_BP_POSITION_NAMES = [
    # Translators: Abbreviation for Prime Minister
    [ugettext_lazy("PM"),
    # Translators: Abbreviation for Deputy Prime Minister
     ugettext_lazy("DPM")],
    # Translators: Abbreviation for Leader of the Opposition
    [ugettext_lazy("LO"),
    # Translators: Abbreviation for Deputy Leader of the Opposition
     ugettext_lazy("DLO")],
    # Translators: Abbreviation for Member for the Government
    [ugettext_lazy("MG"),
    # Translators: Abbreviation for Government Whip
     ugettext_lazy("GW")],
    # Translators: Abbreviation for Member for the Opposition
    [ugettext_lazy("MO"),
    # Translators: Abbreviation for Opposition Whip
     ugettext_lazy("OW")]
]


def side_and_position_names(tournament):
    """Yields 2-tuples (side, positions), where position is a list of position
    names, all being translated human-readable names. This should eventually
    be extended to return an appropriate list for the tournament configuration.
    """
    sides = [get_side_name(tournament, side, 'full').title() for side in tournament.sides]

    if tournament.pref('teams_in_debate') == 'bp' \
            and tournament.last_substantive_position == 2 \
            and tournament.reply_position is None:

        for side, positions in zip(sides, _BP_POSITION_NAMES):
            yield side, positions

    else:
        for side in sides:
            positions = [_("Reply") if pos == tournament.reply_position
                else _ORDINALS[pos]
                for pos in tournament.positions]
            yield side, positions

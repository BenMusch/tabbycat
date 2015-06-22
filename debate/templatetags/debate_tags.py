from django import template
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.conf import settings
from django.core.urlresolvers import reverse
from debate.emoji import EMOJI_LIST

import re
import os

register = template.Library()

STATIC_PATH = settings.MEDIA_ROOT
version_cache = {}

rx = re.compile(r'^(.*)\.(.*?)$')
def version(path_string, base_url=settings.MEDIA_URL):

    if not hasattr(settings, 'ENABLE_MEDIA_VERSIONING') or not settings.ENABLE_MEDIA_VERSIONING:
        return base_url + path_string

    try:
        if path_string in version_cache:
            mtime = version_cache[path_string]
        else:
            mtime = os.path.getmtime(os.path.join(settings.MEDIA_ROOT, path_string))
            version_cache[path_string] = mtime

        return base_url + rx.sub(r'\1.%d.\2' % mtime, path_string)
    except:
        return base_url + path_string
register.simple_tag(version)

def aff_count(team, round):
    if round is None:
        return 0
    return team.get_aff_count(round.seq)
register.simple_tag(aff_count)

def neg_count(team, round):
    if round is None:
        return 0
    return team.get_neg_count(round.seq)
register.simple_tag(neg_count)

def team_emoji(team):
    if team.emoji_seq:
        return b"%s" % EMOJI_LIST[team.emoji_seq]
    else:
        if team.id > len(EMOJI_LIST):
            return b"%s" % EMOJI_LIST[(team.id % len(EMOJI_LIST))] # Wrapping around if too high
        else:
            return b"%s" % EMOJI_LIST[team.id]
register.simple_tag(team_emoji)


def team_status_classes(team):
    classes = ""
    if team.region is not None:
        region_stripped = team.region.name.replace(' ', '_')
        classes += "region-%s" % region_stripped
    if team.esl:
        classes += " language-esl"
    if team.efl:
        classes += " language-efl"
    return classes
register.simple_tag(team_status_classes)


def debate_draw_status_class(debate):
    if debate.aff_team.type == 'B' or debate.neg_team.type == 'B':
        return "active text-muted"
    elif debate.result_status == "P":
        return "active text-muted"
    elif debate.confirmed_ballot:
        if debate.confirmed_ballot.forfeit:
            return "active text-muted"

register.simple_tag(debate_draw_status_class)



class RoundURLNode(template.Node):
    def __init__(self, view_name, round=None):
        self.view_name = view_name
        self.round = round

    def render(self, context):
        if self.round:
            round = self.round.resolve(context)
        else:
            round = context['round']
        return reverse(self.view_name, args=[round.tournament.slug,
                                             round.seq],
                       current_app=context.current_app)

class TournamentURLNode(template.Node):
    def __init__(self, view_name, args):
        self.view_name = view_name
        self.args = args

    def render(self, context):
        args=[context['tournament'].slug]
        args.extend(a.resolve(context) for a in self.args)
        args = tuple(args)
        return reverse(self.view_name, args=args,
                       current_app=context.current_app)

@register.tag
def round_url(parser, token):
    bits = token.split_contents()
    if len(bits) == 3:
        round = parser.compile_filter(bits[2])
    else:
        round = None
    return RoundURLNode(bits[1], round)

@register.tag
def tournament_url(parser, token):
    bits = token.split_contents()

    args = tuple([parser.compile_filter(b) for b in bits[2:]])
    return TournamentURLNode(bits[1], args)

@register.filter
def next_value(value, arg):
    try:
        return value[int(arg)+1]
    except:
        return None

@register.filter
def prev_value(value, arg):
    try:
        return value[int(arg)-1]
    except:
        return None

@register.filter(name='times')
def times(number):
    return range(number)
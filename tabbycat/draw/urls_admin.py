from django.conf.urls import url

from . import views

urlpatterns = [

    # Creation/Release
    url(r'^round/(?P<round_seq>\d+)/$',
        views.AdminDrawView.as_view(),
        name='draw'),
    url(r'^round/(?P<round_seq>\d+)/create/$',
        views.CreateDrawView.as_view(),
        name='draw-create'),
    url(r'^round/(?P<round_seq>\d+)/details/$',
        views.AdminDrawWithDetailsView.as_view(),
        name='draw-details'),
    url(r'^round/(?P<round_seq>\d+)/position-balance/$',
        views.PositionBalanceReportView.as_view(),
        name='draw-position-balance'),
    url(r'^round/(?P<round_seq>\d+)/confirm/$',
        views.ConfirmDrawCreationView.as_view(),
        name='draw-confirm'),
    url(r'^round/(?P<round_seq>\d+)/regenerate/confirm/$',
        views.ConfirmDrawRegenerationView.as_view(),
        name='draw-confirm-regenerate'),
    url(r'^round/(?P<round_seq>\d+)/regenerate/$',
        views.DrawRegenerateView.as_view(),
        name='draw-regenerate'),

    # Side Editing
    url(r'^sides/$',
        views.SideAllocationsView.as_view(),
        name='draw-side-allocations'),
    url(r'^round/(?P<round_seq>\d+)/matchups/edit/$',
        views.EditMatchupsView.as_view(),
        name='draw-matchups-edit'),
    url(r'^round/(?P<round_seq>\d+)/matchups/save/$',
        views.SaveDrawMatchupsView.as_view(),
        name='save-debate-teams'),
    url(r'^round/(?P<round_seq>\d+)/sides/save/$',
        views.SaveDebateSidesStatusView.as_view(),
        name='save-debate-sides-status'),

    # Display
    url(r'^round/(?P<round_seq>\d+)/display/$',
        views.AdminDrawDisplay.as_view(),
        name='draw-display'),
    url(r'^round/(?P<round_seq>\d+)/display-by-venue/$',
        views.AdminDrawDisplayForRoundByVenueView.as_view(),
        name='draw-display-by-venue'),
    url(r'^round/(?P<round_seq>\d+)/display-by-team/$',
        views.AdminDrawDisplayForRoundByTeamView.as_view(),
        name='draw-display-by-team'),
    url(r'^round/(?P<round_seq>\d+)/release/$',
        views.DrawReleaseView.as_view(),
        name='draw-release'),
    url(r'^round/(?P<round_seq>\d+)/unrelease/$',
        views.DrawUnreleaseView.as_view(),
        name='draw-unrelease'),

    # Scheduling
    url(r'^round/(?P<round_seq>\d+)/schedule/$',
        views.ScheduleDebatesView.as_view(),
        name='draw-schedule-debates'),
    url(r'^round/(?P<round_seq>\d+)/schedule/save/$',
        views.ApplyDebateScheduleView.as_view(),
        name='draw-schedule-apply'),
    url(r'^round/(?P<round_seq>\d+)/confirms/$',
        views.ScheduleConfirmationsView.as_view(),
        name='draw-schedule-confirmations'),
    url(r'^round/(?P<round_seq>\d+)/start-time/set/$',
        views.SetRoundStartTimeView.as_view(),
        name='draw-start-time-set'),

]

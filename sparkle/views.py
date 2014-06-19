from django.shortcuts import render, get_object_or_404
from sparkle.models import Application, SystemProfileReport, SystemProfileReportRecord


def appcast(request, application_slug):
    """Generate the appcast for the given application while recording any
    system profile reports"""

    application = get_object_or_404(Application, slug=application_slug)

    # if there are get parameters from the system profiling abilities
    if len(request.GET):
        # create a report and records of the keys/values
        report = SystemProfileReport.objects.create(
            ip_address=request.META.get('REMOTE_ADDR'),
        )
        for key, value in request.GET.iteritems():
            SystemProfileReportRecord.objects.create(
                report=report, key=key, value=value
            )

    return render(request, 'sparkle/appcast.xml', {'application': application})

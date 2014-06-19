from django.views.generic.detail import DetailView
from .models import Application, SystemProfileReport, SystemProfileReportRecord


class AppcastView(DetailView):

    model = Application
    context_object_name = 'application'
    content_type = 'application/xml'
    template_name = 'sparkle/appcast.xml'

    def render_to_response(self, context, **response_kwargs):
        """Record system profile reports before we send out the response.
        """
        if self.request.GET:
            # Create a report and records of the keys/values
            report = SystemProfileReport.objects.create(
                ip_address=self.request.META.get('REMOTE_ADDR'),
            )
            for key in self.request.GET:
                SystemProfileReportRecord.objects.create(
                    report=report, key=key, value=self.request.GET[key],
                )
        return super(AppcastView, self).render_to_response(
            context, **response_kwargs
        )


appcast = AppcastView.as_view()

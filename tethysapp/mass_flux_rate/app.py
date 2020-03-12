from tethys_sdk.base import TethysAppBase, url_map_maker


class MassFluxRate(TethysAppBase):
    """
    Tethys app class for Mass Flux Rate.
    """

    name = 'Mass Flux Rate'
    index = 'mass_flux_rate:home'
    icon = 'mass_flux_rate/images/icon.gif'
    package = 'mass_flux_rate'
    root_url = 'mass-flux-rate'
    color = '#8e44ad'
    description = 'Calculating mass flux in Hawaii'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='mass-flux-rate',
                controller='mass_flux_rate.controllers.home'
            ),
        )

        return url_maps

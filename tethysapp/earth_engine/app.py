from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting

class EarthEngine(TethysAppBase):
    """
    Tethys app class for Automated Inundation Mapper.
    """

    name = 'Automated Inundation Mapper'
    index = 'earth_engine:home'
    icon = 'earth_engine/images/icon.png'
    package = 'earth_engine'
    root_url = 'earth-engine'
    color = '#524745'
    description = 'This tool generates time series of surface water extents using satellite imagery.'
    tags = '"Inundation Extent", "Surface Water", "Shapefile", "Time series"'
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
                url='earth-engine',
                controller='earth_engine.controllers.home'
            ),
	    UrlMap(
            	name='get_image_collection',
            	url='earth-engine/get-image-collection',
            	controller='earth_engine.controllers.get_image_collection'
	    ),
            UrlMap(
            	name='get_time_series_plot',
            	url='earth-engine/get-time-series-plot',
            	controller='earth_engine.controllers.get_time_series_plot'
	    ),
        )

        return url_maps

    def custom_settings(self):
    	"""
    	Custom settings.
    	"""
    	custom_settings = (
        	CustomSetting(
            		name='service_account_email',
            		type=CustomSetting.TYPE_STRING,
            		description='Email associated with the service account.',
            		default='',
            		required=False,
        	),
        	CustomSetting(
            		name='private_key_file',
            		type=CustomSetting.TYPE_STRING,
            		description='Path to service account JSON file containing the private key.',
            		default='',
            		required=False,
        	),
    	)
    	return custom_settings

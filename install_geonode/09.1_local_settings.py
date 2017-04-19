import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

SITEURL = "http://localhost/"
SITENAME = ""

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '::1']
PROXY_ALLOWED_HOSTS = ("127.0.0.1", 'localhost', '::1')
POSTGIS_VERSION = (2, 2, 1)

# Add csv to default document types for upload
# Also 3ws and fbx (3D file formats)
# Remove entries we don't need as the list is getting unwieldy
#ALLOWED_DOCUMENT_TYPES = ['3ws', 'csv', 'doc', 'docx', 'fbx', 'gif', 'gz', 'jpeg', 'jpg', 'odp', 'ods', 'odt', 'pdf', 'png',
#                          'ppt', 'pptx', 'rar', 'sld', 'tif', 'tiff', 'txt', 'xls', 'xlsx', 'xml', 'zip']
ALLOWED_DOCUMENT_TYPES = ['3ws', 'csv', 'doc', 'docx', 'fbx', 'gif', 'jpg', 'pdf', 'png',
                          'ppt', 'pptx', 'txt', 'xls', 'xlsx', 'zip']

# Email for users to contact admins.
THEME_ACCOUNT_CONTACT_EMAIL = "admin@example.com"

DATABASES = {
    'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'geonode',
         'USER': 'geonode',
         'PASSWORD': 'geonode',
     },
    # vector datastore for uploads
    'datastore' : {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        #'ENGINE': '', # Empty ENGINE name disables
        'NAME': 'geonode_data',
        'USER' : 'geonode',
        'PASSWORD' : 'geonode',
        'HOST' : 'localhost',
        'PORT' : '5432',
    }
}

# OGC (WMS/WFS/WCS) Server Settings
OGC_SERVER = {
    'default' : {
        'BACKEND' : 'geonode.geoserver',
        'LOCATION' : 'http://localhost/geoserver/',
        # Public location must have actual site name, otherwise WMS calls in layer map fails
        # 'PUBLIC_LOCATION' : 'http://localhost/geoserver/',
        'PUBLIC_LOCATION' : '%sgeoserver/' % SITEURL,
        'USER' : 'admin',
        'PASSWORD' : 'geoserver',
        'MAPFISH_PRINT_ENABLED' : True,
        'PRINT_NG_ENABLED' : True,
        'GEONODE_SECURITY_ENABLED' : True,
        'GEOGIG_ENABLED' : False,
        'WMST_ENABLED' : False,
        'BACKEND_WRITE_ENABLED': True,
        'WPS_ENABLED' : False,
        'LOG_FILE': '%s/geoserver/data/logs/geoserver.log' % os.path.abspath(os.path.join(PROJECT_ROOT, os.pardir)),
        # Set to name of database in DATABASES dictionary to enable
        'DATASTORE': 'datastore', #'datastore',
    }
}

CATALOGUE = {
    'default': {
        # The underlying CSW implementation
        # default is pycsw in local mode (tied directly to GeoNode Django DB)
        'ENGINE': 'geonode.catalogue.backends.pycsw_local',
        # pycsw in non-local mode
        # 'ENGINE': 'geonode.catalogue.backends.pycsw_http',
        # GeoNetwork opensource
        # 'ENGINE': 'geonode.catalogue.backends.geonetwork',
        # deegree and others
        # 'ENGINE': 'geonode.catalogue.backends.generic',

        # The FULLY QUALIFIED base url to the CSW instance for this GeoNode
        'URL': '%scatalogue/csw' % SITEURL,
        # 'URL': 'http://localhost:8080/geonetwork/srv/en/csw',
        # 'URL': 'http://localhost:8080/deegree-csw-demo-3.0.4/services',

        # login credentials (for GeoNetwork)
        'USER': 'admin',
        'PASSWORD': 'admin',
    }
}

# Default preview library
#LAYER_PREVIEW_LIBRARY = 'geoext'

# Enable upload of KML, CSV, geoJSON and Zip (?) - according to static/geonode/js/upload/FileTypes.js 
UPLOADER = {
    'BACKEND': 'geonode.importer',
    'OPTIONS': {
        'TIME_ENABLED': False,
        'GEOGIG_ENABLED': False,
    }
}
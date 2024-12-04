from app import app as app
from Upload import upload as upload

# Alias aplikasi
applications = {
    '/api1': app,
    '/api2': upload
}

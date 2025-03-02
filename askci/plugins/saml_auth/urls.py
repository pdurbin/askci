"""

Copyright (C) 2019 Vanessa Sochat.

This Source Code Form is subject to the terms of the
Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed
with this file, You can obtain one at http://mozilla.org/MPL/2.0/.

"""

from django.conf.urls import include, url
import askci.plugins.saml_auth.views as views

urlpatterns = [url(r"^saml.xml$", views.saml_metadata_view, name="samlxml")]

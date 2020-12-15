from conans import ConanFile, tools

class QtCoapConan(ConanFile):
    name = "qtcoap"
    description = "CoAP module for Qt"
    topics = ("conan", "qtcoap", "coap")
    url = "https://github.com/blixttech/conan-qtcoap.git"
    homepage = "https://code.qt.io/cgit/qt/qtcoap.git"
    license = "	LGPL-3.0-only"  # SPDX Identifiers https://spdx.org/licenses/

    python_requires = "qtmodulepyreq/0.1.0@blixt/stable"
    python_requires_extend = "qtmodulepyreq.QtModuleConanBase"

    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = {"shared": True}

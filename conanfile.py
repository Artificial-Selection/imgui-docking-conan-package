from conans import ConanFile, CMake, tools
import os
import shutil

required_conan_version = ">=1.33.0"


class IMGUIConan(ConanFile):
    name = "imgui"
    url = "https://github.com/conan-io/conan-center-index"
    homepage = "https://github.com/ocornut/imgui"
    description = "Bloat-free Immediate Mode Graphical User interface for C++ with minimal dependencies"
    topics = ("conan", "imgui", "gui", "graphical")
    license = "MIT"

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
         "fPIC": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True
    }

#-- Add glad/glfw for backends
    requires = [
        'glad/0.1.34@snv/stable',
        'glfw/3.3.4'
    ]
#--

    _cmake = None

    @property
    def _source_subfolder(self):
        return "source_subfolder"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            del self.options.fPIC

    def source(self):
        tools.get(**self.conan_data["sources"][self.version],
                  destination=self._source_subfolder, strip_root=True)

#-- Copy backend files
        backends_folder = os.path.join(self._source_subfolder, "backends")
        backends_files = [
            "imgui_impl_glfw",
            "imgui_impl_opengl3",
        ]
        
        for file_name in backends_files:
            shutil.move(os.path.join(backends_folder, f'{file_name}.h'), self._source_subfolder)
            shutil.move(os.path.join(backends_folder, f'{file_name}.cpp'), self._source_subfolder)
#--

    def _configure_cmake(self):
        if self._cmake:
            return self._cmake
        self._cmake = CMake(self)
        self._cmake.configure()
        return self._cmake

    def build(self):
        cmake = self._configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE.txt", dst="licenses", src=self._source_subfolder)
        cmake = self._configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["imgui"]
        if self.settings.os == "Linux":
            self.cpp_info.system_libs.append("m")

        bin_path = os.path.join(self.package_folder, "bin")
        self.output.info("Appending PATH env var with : {}".format(bin_path))
        self.env_info.PATH.append(bin_path)

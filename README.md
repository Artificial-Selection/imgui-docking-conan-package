# imgui-docking-conan-package

## Info

Conan package of [ImGui 'docking' branch](https://github.com/Artificial-Selection/imgui/releases/tag/18311_docking)
  - Built with glfw and custom [glad](https://github.com/Artificial-Selection/glad-conan-package) package
  - `[Debug, Release]` build types
  - Added additional sources/headers to `imgui.lib`
    - `imgui_impl_glfw.*`
    - `imgui_impl_opengl3.*`
  - conan package uploaded to [GitLab repo](https://gitlab.com/Artificial-Selection/conan-packages/-/packages)

## Usage

1. Add remote GitLab repo to conan
  ```
  conan remote add gitlab https://gitlab.com/api/v4/projects/28364651/packages/conan
  ```

2. Add `imgui/18311@snv/docking` package to conan requires

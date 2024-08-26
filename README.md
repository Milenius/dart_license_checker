# Dart License Checker

Shows you which licenses your dependencies have.

```
┌───────────────────────────┐
│ Package Name  License     │
├───────────────────────────┤
│     barbecue  Apache 2.0  │
│         pana  BSD         │
│         path  BSD         │
│pubspec_parse  BSD         │
│         tint  MIT         │
└───────────────────────────┘
```

## Install

`flutter pub global activate dart_license_checker`

## Use

- Make sure you are in the main directory of your Flutter app or Dart program
- Execute `dart run dart_license_checker.dill`

If this doesn't work, you may need to set up your PATH (see https://dart.dev/tools/pub/cmd/pub-global#running-a-script-from-your-path)

## Building

run `dart compile kernel bin/dart_license_checker.dart` to build the executable `dart_license_checker.dill`.

## Showing transitive dependencies

By default, `dart_license_checker` only shows immediate dependencies (the packages you list in your `pubspec.yaml`).

If you want to analyze transitive dependencies too, you can use the `--show-transitive-dependencies` flag:

`dart_license_checker --show-transitive-dependencies`

## Misc

- The content in the `utils/` directory can be safely ignored. It's use is deprecated, but could be rewritten to be used in the future.
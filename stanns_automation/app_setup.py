# flutter_webview_setup.py
'''
flutter_setup_guide = """
To build home page:
https://stanns.tatotechnologies.com/pages/16/build

Flutter APK:

1. Unzip the file and place it into Android Studio.
2. Change the logo at:
   C:\Users\veera\StudioProjects\webview_to_android_app\android\app\src\main\res
3. Change the login URL at line 39 in `webview_screen.dart`.
4. Change the school app name at line 9 in `AndroidManifest.xml`.

Creating a new Flutter WebView app:

1. Create a new Flutter project with the school name and package as `com.tato.school_name`.
2. Copy and paste `webview_screen.dart` and `splash_screen.dart` files into the `lib` folder.
3. Copy and paste the `res` folder.
4. In `AndroidManifest.xml`, add:
   <uses-permission android:name="android.permission.INTERNET"/>
   <uses-permission android:name="android.permission.CAMERA"/>
   <uses-permission android:name="android.permission.RECORD_AUDIO"/>
   <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>
   <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>
5. Change the label name in `<application>` tag.
6. In `app/build.gradle`, change:
   ndkVersion to "27.0.12077973"
7. In `pubspec.yaml`, add:
   dependencies:
     flutter_inappwebview: ^6.0.0
     permission_handler: ^11.3.1

   dev_dependencies:
     flutter_native_splash: ^2.4.0

   flutter:
     assets:
       - assets/Ascent_logo.png
       - assets/logo.png

   flutter_native_splash:
     color: "#f6dff7"
     image: assets/Ascent_logo.png
     branding: assets/logo.png
     branding_mode: bottom
     android: true
     ios: true
     web: false
8. Copy and paste the `assets` folder.
9. In `main.dart`, paste:

import 'package:flutter/material.dart';
import 'package:flutter_native_splash/flutter_native_splash.dart';
import 'package:webview_school_app/splash_screen.dart';
import 'webview_screen.dart';

void main() async {
  final widgetsBinding = WidgetsFlutterBinding.ensureInitialized();
  FlutterNativeSplash.preserve(widgetsBinding: widgetsBinding);

  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: SplashScreen(),
    );
  }
}

Run the following commands:
flutter clean
flutter pub get
dart run flutter_native_splash:create
flutter build apk --release

Firebase Integration (source: https://www.youtube.com/watch?v=FYcYVkTowRs):

1. Create a Firebase project for your app.
2. Download `google-services.json` and place it in the app-level directory.
3. In project-level `build.gradle`, under `buildscript`:

buildscript {
    repositories {
        google()
        jcenter()
    }
    dependencies {
        classpath("com.google.gms:google-services:4.4.2")
    }
}

4. In app-level `build.gradle`, under `plugins`:
   id("com.google.gms.google-services")

   Add to dependencies block:
   implementation("com.google.firebase:firebase-analytics")

Preparing to upload to Play Store:

1. Generate keystore:

keytool -genkey -v -keystore upload-keystore.jks -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias upload

Example with path:
keytool -genkey -v -keystore C:\Users\veera\StudioProjects\keys\stanns\key.jks -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias key

Privacy Policy:
https://sites.google.com/view/stanns-policy
"""

with open("flutter_webview_setup.py", "w") as file:
    file.write(f""""""{flutter_setup_guide}""""")
'''
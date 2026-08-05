# 478 Relax

A beautiful, minimalist breathwork app that guides you through the 4-7-8 breathing technique for relaxation, stress relief, and better sleep.

![Platform: iOS](https://img.shields.io/badge/platform-iOS-lightgrey)
![Built with Expo](https://img.shields.io/badge/built%20with-Expo-blue)
![TypeScript](https://img.shields.io/badge/language-TypeScript-blue)

---

## ⚠️ Important: Development Version

**This is a DEVELOPMENT version of the app, not a production build.**

### What This Means

| Aspect | Development Version (This) | Production Build |
|--------|---------------------------|------------------|
| How to run | Requires local server on your computer | Standalone app on your phone |
| Command | `npx expo start --tunnel` | `eas build --platform ios` |
| Requires | Computer running + Expo Go app | Just the installed app |
| Best for | Testing, development | Distribution to users |

### To Run This Development Version

1. **On your computer** (must stay running):
   ```bash
   cd 478-relax
   npm install
   npx expo start --tunnel
   ```

2. **On your iPhone**:
   - Install "Expo Go" from App Store
   - Scan the QR code shown in your terminal

3. **Keep your computer running** - if you close the terminal or shut down your computer, the app stops working on your phone.

### To Create a Production Build (Standalone App)

If you want an app that works independently without a computer:

```bash
# Requires Apple Developer Account ($99/year)
npm install -g eas-cli
eas login
eas build --platform ios --profile production
```

See [docs/EXPO_DEMYSTIFIED.md](docs/EXPO_DEMYSTIFIED.md) for detailed instructions.

---

## What is 4-7-8 Breathing?

The 4-7-8 breathing technique is a powerful relaxation method developed by Dr. Andrew Weil:

- **Inhale** through your nose for **4 seconds**
- **Hold** your breath for **7 seconds**
- **Exhale** through your mouth for **8 seconds**

This pattern activates your parasympathetic nervous system, naturally calming your body and mind.

---

## Features

- **Visual Guide**: Animated circle expands and contracts with your breath
- **Haptic Feedback**: Gentle vibration each second (optional)
- **Sound Feedback**: Soft tick sound each second (optional)
- **Customizable Cycles**: 1-5 rounds or infinite mode
- **Dark Theme**: Easy on the eyes, perfect for bedtime
- **Persistent Settings**: Your preferences are saved

---

## Quick Start

### For Users

1. Download **Expo Go** from the App Store
2. Scan the QR code provided by the developer
3. Tap the circle to start breathing
4. Follow the visual cues: grow = inhale, hold, shrink = exhale

📖 **Full User Guide**: [docs/USER_GUIDE.md](docs/USER_GUIDE.md)

### For Developers

```bash
# Clone/download the project
cd 478-relax

# Install dependencies
npm install

# Start development server
npx expo start --tunnel

# Scan QR code with Expo Go app
```

📖 **Full Developer Guide**: [docs/DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md)

---

## Documentation

| Document | Audience | Description |
|----------|----------|-------------|
| [USER_GUIDE.md](docs/USER_GUIDE.md) | End Users | How to use the app, 10 exercises, tips |
| [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) | Developers | Complete setup and coding guide |
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Developers | Technical deep-dive |
| [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Everyone | Common issues and solutions |
| [EXPO_DEMYSTIFIED.md](docs/EXPO_DEMYSTIFIED.md) | Developers | How Expo works under the hood |
| [CLAUDE.md](CLAUDE.md) | AI Assistants | Instructions for AI coding help |

---

## Project Structure

```
478-relax/
├── app/                    # Screens (Expo Router)
│   ├── _layout.tsx         # Root layout
│   ├── index.tsx           # Main breathing screen
│   └── settings.tsx        # Settings modal
├── components/             # Reusable UI components
├── hooks/                  # Custom React hooks
├── constants/              # Configuration values
├── types/                  # TypeScript definitions
├── assets/                 # Images, sounds
└── docs/                   # Documentation
```

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| [React Native](https://reactnative.dev) | Mobile app framework |
| [Expo](https://expo.dev) | Development platform |
| [TypeScript](https://typescriptlang.org) | Type-safe JavaScript |
| [Expo Router](https://expo.github.io/router) | File-based navigation |
| [Reanimated](https://docs.swmansion.com/react-native-reanimated/) | Smooth animations |
| [expo-audio](https://docs.expo.dev/versions/latest/sdk/audio/) | Sound playback |
| [expo-haptics](https://docs.expo.dev/versions/latest/sdk/haptics/) | Vibration feedback |

---

## Development Commands

```bash
# Start development server
npx expo start

# Start with tunnel (works from anywhere)
npx expo start --tunnel

# Clear cache and start
npx expo start --clear

# Check TypeScript
npx tsc --noEmit

# Install Expo-compatible package
npx expo install <package-name>
```

---

## Building for Production

### Using EAS (Expo Application Services)

```bash
# One-time setup
npm install -g eas-cli
eas login
eas build:configure

# Build for iOS
eas build --platform ios --profile production

# Submit to App Store
eas submit --platform ios
```

📖 See [EXPO_DEMYSTIFIED.md](docs/EXPO_DEMYSTIFIED.md) for detailed build instructions.

---

## Contributing

1. Read the [Developer Guide](docs/DEVELOPER_GUIDE.md)
2. Make changes in a feature branch
3. Run `npx tsc --noEmit` to check for errors
4. Test on a physical device
5. Submit a pull request

---

## Future Enhancements

- [ ] Multiple breathing patterns (Box, 5-5-5, custom)
- [ ] Session history and statistics
- [ ] Apple Watch companion
- [ ] Widgets for quick access
- [ ] Guided audio instructions
- [ ] Ambient background sounds
- [ ] Light/dark theme toggle

---

## License

MIT License - Feel free to use and modify for your own projects.

---

## Acknowledgments

### Inspiration
This application was inspired by [Vibe coding a mobile app with Claude Opus 4.5](https://www.ai-supremacy.com/p/vibe-coding-a-mobile-app-with-claude-opus-4-5) by Michael Spencer.

### AI-Generated Content
**All code and documentation in this project were generated by [Claude Code](https://claude.ai/claude-code) powered by Claude Opus 4.5.**

This includes:
- All TypeScript/React Native source code
- All documentation (~5,500 lines across 9 documents)
- Project configuration files
- This README

### Other Credits
- Dr. Andrew Weil for the 4-7-8 breathing technique
- Expo team for the amazing development platform
- React Native community for the ecosystem

---

**Breathe well. Live well.** 🧘

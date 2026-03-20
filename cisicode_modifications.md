# Cisicode

Cisicode is a modified version of Aider that operates independently of Aider's servers.

## Modifications

The following changes have been made to ensure independence:

1.  **Version Checking Disabled:** The application will no longer check PyPI for updates or prompt you to upgrade.
2.  **Analytics Disabled:** Analytics collection (PostHog/Mixpanel) has been permanently disabled in the code.
3.  **Model Cache Updates Disabled:** The application will not download the latest model metadata (prices, context windows) from the `litellm` repository. It will use the bundled metadata.
4.  **Release Notes Disabled:** The application will not offer to show release notes on the first run of a new version.

## Usage

Run cisicode as you normally would:

```bash
cisicode --model azure/o4-mini
```

## Note on Updates

Since automatic updates and version checking are disabled, you will need to manually update the codebase if you wish to use a newer version of the underlying Aider logic.

# SLCB WordsAPI

WOrdsAPI Parameter allows for creating custom commands to get WordsAPI info on 
a word for use in custom commands as a parameter. Currently only defintions and pronunciation are returned
but it could easily be expanded to return other information. (synonyms, antonyms, syllables, etc)

## Installing

This script was built for use with Streamlabs Chatbot.
Follow instructions on how to install custom script packs at:
https://github.com/StreamlabsSupport/Streamlabs-Chatbot/wiki/Prepare-&-Import-Scripts

Click [Here](https://github.com/Encrypted-Thoughts/SLCB-WordsAPI/blob/master/WordsAPI.zip?raw=true) to download the script pack.

## Use

Once installed the below parameter can be inserted into custom commands created in SLCB.
In custom script parameters a character length on definition can be set.
This allows long definitions to be limited so the bot doesn't spam chat with multiple messages.

```
$wordsapi(
    string   # Word: The word that the parameter should retrieve the definition of.
)

Example Command: !command add !define $wordsapi($msg)
```

Example in twitch chat:

![image](https://user-images.githubusercontent.com/50642352/85878542-7d1d2800-b79e-11ea-840a-f1d09cdf6654.png)

## Author

EncryptedThoughts - [Twitch](https://www.twitch.tv/encryptedthoughts)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


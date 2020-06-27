# SLCB Dictionary APIs

Adds parameters for various dictionary apis to allow for getting word info in custom commands. 

## Installing

This script was built for use with Streamlabs Chatbot.
Follow instructions on how to install custom script packs at:
https://github.com/StreamlabsSupport/Streamlabs-Chatbot/wiki/Prepare-&-Import-Scripts

Click [Here](https://github.com/Encrypted-Thoughts/SLCB-DictionaryAPI/blob/master/DictionaryAPI.zip?raw=true) to download the script pack.

In order to use this script you'll need to have an account with Rapid API.
https://rapidapi.com/dpventures/api/wordsapi/pricing
You can register for a Free tier at the above link that will allow 2500 requests a day and charge $0.004 per request after that.

Once registered you'll need to find your api key and enter it into the script settings.
https://rapidapi.com/dpventures/api/wordsapi/endpoints

![image](https://user-images.githubusercontent.com/50642352/85913417-33622b00-b7fa-11ea-8351-94b124f6d241.png)

![image](https://user-images.githubusercontent.com/50642352/85881103-b8b9f100-b7a2-11ea-86a6-ba317c46196e.png)

## Use

Once installed the below parameter can be inserted into custom commands created in SLCB.
In custom script parameters a character length on definition can be set.
This allows long definitions to be limited so the bot doesn't spam chat with multiple messages.

```
$wordsapi(
    string   # Word: The word that the parameter should retrieve the definition.,
    string   # Format String: the format the response will be returned in. 
             # Ex: {word} {pronunciation}: {definitions}
)

Example Command: !command add !define $wordsapi($msg, {word} {pronunciation}: {definitions})
```
```
$urban(
    string   # Word: The word that the parameter should retrieve the definition.,
    string   # Format String: the format the response will be returned in. 
             # Ex: {word}: {definition} {link} {thumbs_up} {thumbs_down} {timestamp} {author} {example}
)

Example Command: !command add !define $urban($msg, {word}: {definition} {link} {thumbs_up} {thumbs_down} {timestamp} {author} {example})
```

Example in twitch chat:

![image](https://user-images.githubusercontent.com/50642352/85910515-f2abe700-b7e4-11ea-9e64-313ec7a90e18.png)
<br/>
![image](https://user-images.githubusercontent.com/50642352/85913344-a7500380-b7f9-11ea-8629-6874b6e0f031.png)

## Author

EncryptedThoughts - [Twitch](https://www.twitch.tv/encryptedthoughts)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details


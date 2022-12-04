# FeedbackBot Data Upload Example

This is an example game data upload script for [FeedbackBot](https://www.discordfeedbackbot.com/). You can use
this to upload data, or as a guide for your own data uploader implementation. For questions about FeedbackBot, see
the [documentation page](https://www.discordfeedbackbot.com/docs/#Data%20Lookup) or visit the [FeedbackBot Development Discord](https://discord.gg/788XscP).

## Using this Script.

If you are comfortable running Python 3 scripts, you can use the data_uploader_example.py script to upload game data.

In order to use the script you will need to have the requests library installed, you can do that using

`pip install requests`


To upload the included "game_data.json" file, run the python script and follow the prompts, entering your own upload URL and auth token.

Example:

    $ python data_uploader_example.py

    Please enter the name of the file to upload.
    > game_data.json
    Please enter your auth token.
    > [ENTER YOUR AUTH TOKEN]
    <Response [200]>: Successfully uploaded new lookup data.

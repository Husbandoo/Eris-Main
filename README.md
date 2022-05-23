<h2 align="center">
    ──「Eris Boreas Greyrat」──
</h2>

<p align="center">
  <img src="https://te.legra.ph/file/9abdbb8e7fa75e03a91ea.jpg">
</p>

<p align="center">
<a href="https://app.codacy.com/gh/Awesome-Prince/NekoRobot?utm_source=github.com&utm_medium=referral&utm_content=Awesome-Prince/NekoRobot&utm_campaign=Badge_Grade_Settings" alt="Codacy Badge">
<img src="https://api.codacy.com/project/badge/Grade/6141417ceaf84545bab6bd671503df51" /> </a>
<a href="https://github.com/Husbandoo/eris-main" alt="Libraries.io dependency status for GitHub repo"> <img src="https://img.shields.io/librariesio/github/animekaizoku/SaitamaRobot" /> </a>
</p>
<p align="center">
<a href="https://github.com/Husbandoo/eris-main" alt="GitHub release (latest by date including pre-releases)"> <img src="https://img.shields.io/github/v/release/animekaizoku/saitamarobot?include_prereleases?style=flat&logo=github" /> </a>
<a href="https://www.python.org/" alt="made-with-python"> <img src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?style=flat&logo=python&color=blue" /> </a>
<a href="https://t.me/Husbandoo" alt="Owner!"> <img src="https://aleen42.github.io/badges/src/telegram.svg" /> </a>

## Starting the bot.

Once you've setup your database and your configuration (see below) is complete, simply run:

`python3 -m NekoRobot`

## Deploy
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Husbandoo/Project-Eris) 

## Setting up the bot (Read this before trying to use!):
Please make sure to use python3.6, as I cannot guarantee everything will work as expected on older python versions!
This is because markdown parsing is done by iterating through a dict, which are ordered by default in 3.6.

### Configuration

There are two possible ways of configuring your bot: a config.py file, or ENV variables.

The prefered version is to use a `config.py` file, as it makes it easier to see all your settings grouped together.
This file should be placed in your `NekoRobot` folder, alongside the `__main__.py` file . 
This is where your bot token will be loaded from, as well as your database URI (if you're using a database), and most of 
your other settings.

It is recommended to import sample_config and extend the Config class, as this will ensure your config contains all 
defaults set in the sample_config, hence making it easier to upgrade.

An example `config.py` file could be:
```
from NekoRobot.sample_config import Config

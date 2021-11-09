# r.wcyat.me

Code for [r.wcyat.me](https://r.wcyat.me)/[l.wcyat.me](https://l.wcyat.me), redirection site. Automated with telegram bot.

Create your shortened links on telegram: [t.me/rwcyatmebot](https://t.me/rwcyatmebot)

You should need to edit some code, at least push.sh and add your token (and user id) in main.py.

IT MUST BE RUN ON LINUX / UNIX

# Usage

Execute the code:

```
python3 main.py
```

You need to have pip and python3 installed.

## Telegram bot

<pre>
/create path link: create a directory containing an index.html which redirects to the link.
For root directory, use:  /create . link

/rm path: remove a directory

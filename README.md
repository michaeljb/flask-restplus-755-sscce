# FRP-SSCCE

This is an [SSCCE](http://www.sscce.org/) for an issue I have encountered with
[flask-restplus v0.13.0](https://github.com/noirbizarre/flask-restplus). Issue
link: https://github.com/noirbizarre/flask-restplus/issues/755

When the Swagger location can be accessed via different URLs due to proxy (e.g.,
nginx or Apache) configuration, flask-restplus caches the `basePath` value based
on whichever URL is first used to access the Swagger page. Thus, when the
Swagger page is accessed via a different URL, it receives the `basePath` for the
other one, preventing any sample requests on the page from working.

## Requirements

* Docker 17.09.0+
* ports 80, 443, and 5000 on your localhost must be available

## Running

1) Run `docker-compose up --build` from the root of this repository.
2) Go to https://localhost/, tell the browser to allow the security exception;
   you should see the rendered contents of `./nginx/index.html`
3) On that page, there are two links; whichever is clicked first will determine
   the `basePath` used by `flask-restplus`
4) Follow both links, note the Base URL at the top of the page; try out the `GET
   /hello/` endpoint; whichever was opened first should work and the other won't
5) Stop the server and repeat, but open the links in a different order; you
   should see a different value for the Base URL (the two possible values are
   `/` and `/api`)


## Demo

I took a screen recording of myself going through the steps above
(`demo.mov`). The whole video is 4 minutes long, but the first 2:35 is just the
containers being built and the stack starting for the first time.

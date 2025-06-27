# Open source examples

!!! info

    **Status**: WIP RFC
    
    **Level**: 2

    **Updated**: 2025-06-27

## Summary

I've created a bunch of free open source examples of software engineering, and I
intend to use with our staff for teaching and training, such as for test automation.

Some organizations have some people who have questions about open source, so
this ADR is to help describe how it works, and the specifics that I'm doing with
staff, so any stakeholder can ask questions, add advice, and participate.

## Drivers

Right now I need qto teach and train our operations testers in how to do test
automation. A specific example is how to use Selenium browser automation to
visit a web URL, inspect what the page shows, and report success or failure.

I intend to use my pre-existing free open source software to help with this,
because I've done this before with other organizations. I have free open source
repositories that demonstrate how to use Selenium for browser testing, and that
provide simple web services that Selenium can query.

The specifics include these free open source repositories to start...

Demonstrations of how to use Selenium with JavaScript, Python, etc.

* <https://github.com/joelparkerhenderson/demo-selenium-javascript>

Web service examples that are targets that Selenium can test, such as this web
service that prints the current time in unix epoch format:

* <https://github.com/joelparkerhenderson/web-service-epoch-axum>

Testing examples that are web pages with testable user interfaces, such as with
testable HTML tags, CSS styles, etc.

* <https://github.com/testingexamples>

All of these are my own free open source projects, so I'm confident they work.

I've chatted about these broad strokes over a few months with all of our direct
stakeholders i.e. up my chain of command, and also with our services folks such
as some of our internal systems maintainers, some of our security leaders, etc.
This ADR is to provide specifics, so all the stakeholders can look directly at
the goals and options.

## Options

* Yes, good, right

* Maybe, needs improvement

* No, bad, wrong
  
A successful outcome (IMHO) looks like what many of my clients do, which is "We like
using open source. These projects have clear licenses that we know such as MIT
or BSD or GPL. Use the projects. Don't incorporate any of the projects' source
code into our core software without first getting governance clearance."

An unsuccessful outcome (IMHO) looks like what one of my client did, which was
banning the use of external open source projects, in favor of building
internally and buying externally, because those are easier to control legally
for high-stakes auditing.

I'm currently aiming to chat about this with:

* out client services staff (done)

* our organization's risk registry manager (done)

* our CISO (scheduled for next week)

* our CISO deputy (todo)

## Options Analysis

### Yes, good, right

**Pro:**

* Easy
* Friendly
* Fast

**Con:**

* No commerical support
* No commercial maintenance
* No commercial indemnification

### Maybe, needs improvement

**Pros:**

* Could turn up unknown unknowns for learning opportunities

* Might be helpful for creating organization change

* Potentially surfaces ideas for feature improvements

**Cons:**

* Time & money, such as if our org wants legal audits.

### No, bad, wrong

**Pros:**

* Clear
* Direct
* Certain

**Cons:**

* Snowballs into future build-vs-buy investigations

## Recommendation

Yes, good, right.

I like this because I need to teach our operations testers starting near-immediately.

### Consequences

Better, cheaper, faster teaching and training.

Kinder, gentler, nicer ways of working.

Smarter, wiser, larger bon accord with free open source projects worldwide.

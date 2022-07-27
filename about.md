---
layout: page
title: About
permalink: /about/
---
![abouttwo](/assets/about-us.jpg)


We are the official supporters club here in Melbourne for Chelsea FC.
We meet to watch most Chelsea games at The Limerick Arms on Clarendon Street in South Melbourne. We can be contacted by email, Facebook, or Twitter with the links below. Membership is available which comes with many perks. All are welcome, come down to The Limerick Arms and say hello!

Melbourne Chelsea Supporters Club has existed (in some capacity) since the 1990’s. In nearly 30 years it has come a long way, mainly on the back of live TV broadcasts, the internet and social media, but the essence of the group has been built around meeting up at the pub to watch our beloved Chelsea.

Whilst we do meet now at The Limerick Arms, previous places have been The Crafty Squire, The Charles Dickens, and also Fluid Oz, the latter is no longer around. Anyone is welcome to watch the match at the pub with us and usual free, maybe the odd cover charge for a midweek morning match.

We do run a local paid membership, and have done so since 2013. Many members have become good friends through our club.
As part of the membership we have run plenty of functions over the years, as kick off times for Chelsea are not usually too kind for social activity. Indoor Futsal, Xmas Parties, Curry Nights, Pub Crawls and also Foot Golf.
A couple of former player have even made it to our club, Charlie Cooke and Paul Canoville.

- **Secretary**: Russell Saunders
- **Chairman**: John Dady
- **Treasurer**: Daniel Thorne
- **Ex-Offico Member**: Andy Bates
- **Ex-Offico Member**: Matt Patterson
- **Ex-Offico Member**: Jocky Clelland
- **IT Administrator**: Adam Miritis

<br>

<br>

![abouttwo](/assets/about2.jpg)

# Posts

{% for category in site.categories %}
  {% capture cat %}{{ category | first }}{% endcapture %}
  <h3 id="{{cat}}">{{ cat | capitalize }}</h3>
  <ul class="posts-list">
  {% for post in site.categories[cat] %}
    <li>
      <strong>
        <a href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
      </strong>
      <span class="post-date">- {{ post.date | date_to_long_string }}</span>
    </li>
  {% endfor %}
  </ul>
  {% if forloop.last == false %}<hr>{% endif %}
{% endfor %}

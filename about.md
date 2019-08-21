---
layout: page
title: About
permalink: /about/
---

<img src="{{ site.baseurl }}/assets/about-us.jpg" title="Profile Picture" class="profile">

We are the official supporters club here in Melbourne for Chelsea FC. We meet regularly to watch games at The Crafty Squire on the corner of Little Collins Street and Russell Street to watch our beloved boys in blue play.. We can be contacted by email, Facebook, or Twitter with the links below. Membership is available which comes with many perks.  All are welcome, come down to The Crafty Squire and say hello!

- **Secretary**: Russell Saunders
- **Chairman**: Daniel Thorne
- **Treasurer**: Adam Miritis
- **Ex-Offico Member**: Kosta Moussageas
- **Ex-Offico Member**: Andy Bates
- **Ex-Offico Member**: John Dady

{% for category in site.categories %}
  {% capture cat %}{{ category | first }}{% endcapture %}
  <h2 id="{{cat}}">{{ cat | capitalize }}</h2>
  {% for desc in site.descriptions %}
    {% if desc.cat == cat %}
      <p class="desc"><em>{{ desc.desc }}</em></p>
    {% endif %}
  {% endfor %}
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

{% extends "mail_templated/base.tpl" %}

{% block subject %}
Account Activation
{% endblock %}

{% block html %}
http://localhost:8001/account/api/v1/activation/confirm/{{token}}
{% endblock %}
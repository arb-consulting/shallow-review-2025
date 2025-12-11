# Shallow Review Draft

{% for section in sections -%}
## {{ section.title }}

{% for agenda in section.agendas -%}
### {{ agenda.title }}

{% if agenda.one_sentence_summary -%}
**Summary:** {{ agenda.one_sentence_summary }}

{% endif -%}
{% if agenda.theory_of_change -%}
**Theory of Change:** {{ agenda.theory_of_change }}

{% endif -%}
{% if agenda.see_also -%}
**See Also:** {% for ref in agenda.see_also -%}
{{ format_see_also(ref) }}
{%- if not loop.last %}, {% endif -%}
{% endfor %}

{% endif -%}
{% if agenda.orthodox_problems -%}
**Orthodox Problems:** {{ agenda.orthodox_problems }}

{% endif -%}
{% if agenda.target_case -%}
**Target Case:** {{ agenda.target_case }}

{% endif -%}
{% if agenda.broad_approach -%}
**Broad Approach:** {{ agenda.broad_approach }}

{% endif -%}
{% if agenda.some_names -%}
**Key Researchers:** {{ agenda.some_names | join(', ') }}

{% endif -%}
{% if agenda.estimated_ftes -%}
**Estimated FTEs:** {{ agenda.estimated_ftes }}

{% endif -%}
{% if agenda.funded_by -%}
**Funded By:** {{ agenda.funded_by }}

{% endif -%}
{% if agenda.funding_in_2025 -%}
**Funding in 2025:** {{ agenda.funding_in_2025 }}

{% endif -%}
{% if agenda.host_org_structure -%}
**Organization Structure:** {{ agenda.host_org_structure }}

{% endif -%}
{% if agenda.teams -%}
**Teams:** {{ agenda.teams }}

{% endif -%}
{% if agenda.public_alignment_agenda -%}
**Public Alignment Agenda:** [{{ agenda.public_alignment_agenda.title or 'Link' }}]({{ agenda.public_alignment_agenda.url }})

{% endif -%}
{% if agenda.framework -%}
**Framework:** [{{ agenda.framework.title or 'Link' }}]({{ agenda.framework.url }})

{% endif -%}
{% if agenda.critiques -%}
**Critiques:** {% for critique in agenda.critiques -%}
[{{ shorten_title(critique.title, 40) if critique.title else 'Link' }}]({{ critique.url }})
{%- if not loop.last %}, {% endif -%}
{% endfor %}

{% endif -%}
{% if agenda.other_attributes -%}
{% for key, value in agenda.other_attributes.items() -%}
{% if value is string -%}
**{{ key }}:** {{ value }}

{% elif value is iterable and value is not string -%}
**{{ key }}:** {% for item in value -%}
{% if item is string and (item.startswith('http://') or item.startswith('https://')) -%}
{{ format_url(item) }}
{%- else -%}
{{ item }}
{%- endif -%}
{%- if not loop.last %}, {% endif -%}
{% endfor %}

{% else -%}
**{{ key }}:** {{ value }}

{% endif -%}
{% endfor -%}
{% endif -%}
{% if agenda.outputs_in_2025 -%}
**Outputs in 2025** ({{ agenda.outputs_in_2025 | length }} items):
{% for output in agenda.outputs_in_2025 -%}
{{ format_url(output.url) }}
{%- if not loop.last %}, {% endif -%}
{% endfor %}

{% endif -%}
{% if agenda.free_form_text -%}
{{ agenda.free_form_text }}

{% endif -%}
{% if agenda.parsing_issues -%}
**⚠️ Parsing Issues:**
{% for issue in agenda.parsing_issues -%}
- {{ issue }}
{% endfor %}

{% endif -%}
---

{% endfor -%}
{% endfor -%}

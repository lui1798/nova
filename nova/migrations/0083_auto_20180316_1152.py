# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-16 03:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nova', '0082_auto_20180315_1336'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permission',
            options={'permissions': (('access_asset', '\u670d\u52a1\u5668\u7ba1\u7406 access_asset'), ('access_app', '\u5e94\u7528\u7cfb\u7edf\u7ba1\u7406 access_app'), ('access_database', '\u6570\u636e\u5e93\u7ba1\u7406 access_database'), ('access_monitor', '\u76d1\u63a7\u7ba1\u7406 access_monitor'), ('access_task', '\u4efb\u52a1\u7ba1\u7406 access_task'), ('access_file', '\u6587\u4ef6\u7ba1\u7406 access_file'), ('access_log', '\u65e5\u5fd7\u7ba1\u7406 access_log'), ('operate_product', '\u751f\u4ea7\u73af\u5883\u6743\u9650 operate_product'), ('access_command', '\u6267\u884c\u547d\u4ee4\u6743\u9650 access_command'), ('exec_sql', '\u6267\u884cSQL exec_sql'), ('upload_oss_file', '\u8003\u8bd5\u62a5\u540dOSS\u9644\u4ef6\u4e0a\u4f20 upload_oss_file'), ('exec_tax_agent_sql', '\u6267\u884c\u8003\u8bd5\u62a5\u540dSQL exec_tax_agent_sql'))},
        ),
    ]

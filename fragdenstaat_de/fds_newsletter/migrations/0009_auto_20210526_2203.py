# Generated by Django 3.1.8 on 2021-05-26 20:03

from django.db import migrations


def port_to_fds_newsletter(apps, schema_editor):
    OldNewsletter = apps.get_model('newsletter', 'Newsletter')
    Newsletter = apps.get_model('fds_newsletter', 'Newsletter')

    OldSubscription = apps.get_model('newsletter', 'Subscription')
    Subscriber = apps.get_model('fds_newsletter', 'Subscriber')

    Mailing = apps.get_model('fds_mailing', 'Mailing')
    MailingMessage = apps.get_model('fds_mailing', 'MailingMessage')

    nl_mapping = {}
    constraint_map = {}
    for old_newsletter in OldNewsletter.objects.all().order_by('id'):
        newsletter = Newsletter.objects.create(
            slug=old_newsletter.slug,
            title=old_newsletter.title,
            url='',
            sender_email=old_newsletter.email,
            sender_name=old_newsletter.sender,
            visible=old_newsletter.visible
        )
        nl_mapping[old_newsletter.id] = newsletter.id
        Mailing.objects.filter(newsletter=old_newsletter).update(new_newsletter=newsletter)
        constraint_map[newsletter.id] = set()

    for subscription in OldSubscription.objects.all():
        newsletter_id = nl_mapping[subscription.newsletter_id]
        if subscription.user_id:
            key = subscription.user_id
        else:
            key = subscription.email_field.lower()
        if key in constraint_map[newsletter_id]:
            continue
        constraint_map[newsletter_id].add(key)

        subscriber = Subscriber.objects.create(
            newsletter_id=newsletter_id,
            user_id=subscription.user_id,
            name=subscription.name_field or '',
            email=subscription.email_field.lower() if subscription.user_id is None else None,
            created=subscription.create_date,
            activation_code=subscription.activation_code,
            last_activation_sent=None,
            subscribed=(
                subscription.subscribe_date if
                subscription.subscribed and
                subscription.subscribe_date and
                not (
                    subscription.unsubscribed or subscription.unsubscribe_date
                )
                else None
            ),
            unsubscribed=(
                subscription.unsubscribe_date if subscription.unsubscribed else None
            )
        )
        MailingMessage.objects.filter(subscription=subscription).update(subscriber=subscriber)


class Migration(migrations.Migration):

    dependencies = [
        ('fds_newsletter', '0008_auto_20210526_2155'),
    ]

    operations = [
        migrations.RunPython(port_to_fds_newsletter)
    ]

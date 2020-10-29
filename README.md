# Anvil Messaging
A library for [Anvil Applications](https://anvil.works) that provides publish-subscribe
messaging.

## Introduction
This library provides a mechanism for forms (and other components) within an Anvil app
to communicate in a 'fire and forget' manner.

It's an alternative to raising and handling events - instead you 'publish' messages to
a channel and, from anywhere else, you subscribe to that channel and process those
messages as required.

## Installation

  * In your anvil application, create a new module in the client code section and name it 'messaging'
  * Copy the entire content of `client_code/messaging.py` from this repository into your 'messaging' module

## Usage

### Create the Publisher
You will need to create an instance of the Publisher class somewhere in your application
that is loaded at startup.

For example, you might create a client module at the top level of your app called 'common'
with the following content:

```python
from .messaging import Publisher

publisher = Publisher()
```

and then import that module in your app's startup module/form.

By default, the publisher will log each message it receieves to your app's logs (and
the output pane if you're in the IDE). You can disable this if you wish:

```python
from .messaging import Publisher

publisher = Publisher(with_logging=False)
```

### Publish Messages
From anywhere in your app, you can import the publisher and publish messages to a channel.
e.g. Let's create a simple form that publishes a 'hello world' message when it's initiated:

```python
from ._anvil_designer import MyPublishingFormTemplate
from .common import publisher


class MyPublishingForm(MyPublishingFormTemplate):

    def __init__(self, **properties):
        publisher.publish(channel="general", title="Hello world")
	self.init_components(**properties)
```

The publish method also has an optional 'content' argument which can be passed any object.

### Subscribe to a Channel
Also, from anywhere in your app, you can subscribe to a channel on the publisher by
providing a handler function to process the incoming messages.

The handler will be passed a Message object, which has the title and content of the
message as attributes.

e.g. On a separate form, let's subscribe to the 'general' channel and print any 'Hello
world' messages:

```python
from ._anvil_designer import MySubscribingFormTemplate
from .common import publisher


class MySubscribingForm(MySubscribingFormTemplate):
    
    def __init__(self, **properties):
	publisher.subscribe(channel="general", handler=self.general_messages_handler)
        self.init_components(**properties)

    def general_messages_handler(self, message):
	if message.title = "Hello world":
	    print(message.title)
```

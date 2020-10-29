# MIT License

# Copyright (c) 2020 Owen Campbell

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# This software is published at https://github.com/meatballs/anvil-messaging


class Message:
    def __init__(self, title, content=None):
        self.title = title
        self.content = content


class Publisher:
    def __init__(self, with_logging=True):
        self.with_logging = with_logging
        self.handlers = {}

    def publish(self, channel, title, content=None):
        message = Message(title, content)
        for handler in self.handlers[channel]:
            handler(message=message)
        if self.with_logging:
            print(
                f"Published '{message.title}' message on '{channel}' channel to "
                f"{len(self.handlers[channel])} subscriber(s)"
            )

    def subscribe(self, channel, handler):
        if channel not in self.handlers:
            self.handlers[channel] = []
        self.handlers[channel].append(handler)

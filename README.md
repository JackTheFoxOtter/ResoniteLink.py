ResoniteLink.py
===============

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)
[![PyPI Version Info](https://img.shields.io/pypi/v/resonitelink.py?color=blue)](https://pypi.python.org/pypi/resonitelink.py)
[![PyPI Python Version](https://img.shields.io/pypi/pyversions/resonitelink.py?color=blue)](https://pypi.python.org/pypi/resonitelink.py)

A Python wrapper for [ResoniteLink](https://github.com/Yellow-Dog-Man/ResoniteLink) - the WebSocket & JSON based API to interface with Resonite's data model.

# ⚠️ Beta WARNING! ⚠️
This API wrapper is currently in beta (so is ResoniteLink itself). There might be bugs and breaking changes without warning. It's not adviced to use this library for production just yet.

# Library features
- Implementation of the ResoniteLink API in modern Python.
- Fully asynchronous API using `async` / `await` syntax.
- Type-hinted API methods & model classes for the use of static type checkers.
- Simple "high-level" layer with convenience features & abstractions to create scripts and automations easily.
- Abstraction free "low-level" layer for more advanced use-cases like building SDKs.

# Compatibility
- This library requires Python 3.13 or later. Older Python versions are not supported.

# Getting started
Take a look at this example code from [hello_world.py](https://github.com/JackTheFoxOtter/ResoniteLink.py/blob/master/examples/hello_world.py). It will connect to ResoniteLink over WebSocket on the specified port, create a new slot, and attach a `TextRenderer` component with the text "*Hello, world!*" to it. You can enable ResoniteLink and get the port number in the `Session` tab of your Resonite dashboard (if you have the required permissions in the current world).


```py
from resonitelink.models.datamodel import Float3, Field_String
from resonitelink import ResoniteLinkClient, ResoniteLinkWebsocketClient
import asyncio


# Creates a new client that connects to ResoniteLink via websocket.
client = ResoniteLinkWebsocketClient()


@client.on_started
async def on_client_started(client : ResoniteLinkClient):
    """
    This async function is called by the client at the end of its startup sequence.
    You can use it to execute code once the client is up and running!

    """
    # Adds a new slot. Since no parent was specified, it will be added to the world root by default.
    slot = await client.add_slot(name="Hello World Slot", position=Float3(0, 1.5, 0))
    
    # Adds a TextRenderer component to the newly created slot.
    await slot.add_component("[FrooxEngine]FrooxEngine.TextRenderer",
        # Sets the initial value of the string field 'Text' on the component.
        Text=Field_String(value="Hello, world!")
    )
    
    # Stops the client manually. Without this, the client will run forever, which might be desired for some use-cases.
    await client.stop()


# Asks for the current port ResoniteLink is running on.
port = int(input("ResoniteLink Port: "))


# Start the client on the specified port.
asyncio.run(client.start(port))
```
You can see examples for more advanced functionality like importing assets in the [examples directory](https://github.com/JackTheFoxOtter/ResoniteLink.py/tree/master/examples).

# Architecture
The library contains two "layers", which are designed for separate use-cases:

## Layer 0: Messages & Responses
This is the base layer of ResoniteLink.py. It is a **low abstraction** representation of the ResoniteLink JSON protocol. Instead of raw JSON, you're interacting with statically typed dataclasses representing the individual JSON models. Interacting with this layer directly is recommended when you're building lower-level integration on top of ResoniteLink.py, since it's pretty much a 1:1 representation of the underlying protocol.

To interact with this layer directly, you need to construct an instance of the corresponding `Message` model class (for example `AddSlot` or `AddComponent`, the base class is abstract and cannot be used by itself), and pass that instance to the `ResoniteLinkClient.send_message(message)` method of a `ResoniteLinkClient` instance. The coroutine will return an instance of the `Response` class corresponding to your request, or raise a `ResoniteLinkException` if the response indicates an error.

This layer is closely following the official C# reference implementation in how the JSON model classes are structured.

## Layer 1: Message methods & Proxies
This layer builds on top of layer 0, but expands on it with convenience functions and abstraction mechanisms. This is the recommended way to use ResoniteLink.py to write scripts and automations, as it provides a clean and convenient syntax with abstractions designed to keep the code short, clean and easy to reason about.

You're interacting with this layer by using the specific functions of a `ResoniteLinkClient` instance, or the objects returned from those, for example `ResoniteLinkClient.add_slot()` or `SlotProxy.add_component()`. These function don't return the `Response` dataclass instances directly, instead they filter out only the relevant information, like the `asset_uri` you get from uploading an asset, or return a `Proxy` instance for methods that return a reference to a resource.

## JSON model serialization / deserialization
This library currently uses a custom built mechanism for defining and serializing / deserializing JSON model dataclasses on top of the `json` standard library, which can better represent the polymorphic nature of the JSON models used by ResoniteLink. This is currently mostly separate from the ResoniteLink specific functionality. I'm pretty happy with how this turned out and will potentially move this into a separate package in the future.

# Future plans
As is stands today, ResoniteLink.py is not yet complete. The following features are still missing and are what I consider "required" for full release version:

* **Representation of vector types that provides common mathematical operations** (likely using numpy vectors).
* **Statically typed component classes & enums.** Right now, components are not represented by individual classes. In the future I will provide the ability to generate those classes dynamically via ResoniteLink's dynamic reflection API (currently still in development). Due to the dynamic nature of Resonite and shier amount of components, the type classes will **not** be bundled with the API, but a code generator to create them will be. I'll potentially create a separate, automatically updated package for the autogenerated components & enums Resonite provides out of the box. If you want to use static typing for dynamic types though (like those added by mods or future WASM / ProtoFlux modules), you'll need to generate them yourself.
* **Auto-generated library documentation**.

Check out the [issues section](https://github.com/JackTheFoxOtter/ResoniteLink.py/issues) for other plans and the current implementation status.

# No generative AI was used to create this library ...
... and I'd like to keep it that way. **Please refrain from submitting AI generated pull requests**. Additionally, please refrain from using this library in projects that use generative AI to produce content for Resonite. I enjoy this game for seeing cool stuff people have made, not stuff hallucinated by generative AI models. Generative AI doesn't make you more creative, it actively makes you less creative. Try investing your efforts into actually learning new skills and creating things by yourself instead.
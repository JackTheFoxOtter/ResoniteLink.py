from typing import Union

from resonitelink.models.datamodel import Member, Slot, Reference, Float3, FloatQ
from resonitelink.proxies import Proxy, ComponentProxy


__all__ = (
    'SlotProxy',
)


class SlotProxy(Proxy[Slot]):
    
    async def fetch_data(self) -> Slot:
        return await self.client.get_slot(self.id)
    
    async def set_parent(self, parent : Union[str, Slot, 'SlotProxy', Reference]):
        await self.client.update_slot(slot=self.id, parent=parent)
        self.invalidate_data()

    async def set_position(self, position : Float3):
        await self.client.update_slot(slot=self.id, position=position)
        self.invalidate_data()
    
    async def set_rotation(self, rotation : FloatQ):
        await self.client.update_slot(slot=self.id, rotation=rotation)
        self.invalidate_data()

    async def set_scale(self, scale : Float3):
        await self.client.update_slot(slot=self.id, scale=scale)
        self.invalidate_data()

    async def set_active(self, is_active : bool):
        await self.client.update_slot(slot=self.id, is_active=is_active)
        self.invalidate_data()

    async def set_persistent(self, is_persistent : bool):
        await self.client.update_slot(slot=self.id, is_persistent=is_persistent)
        self.invalidate_data()

    async def set_name(self, name : str):
        await self.client.update_slot(slot=self.id, name=name)
        self.invalidate_data()
    
    async def set_tag(self, tag  : str):
        await self.client.update_slot(slot=self.id, tag=tag)
        self.invalidate_data()

    async def set_order_offset(self, order_offset : int):
        await self.client.update_slot(slot=self.id, order_offset=order_offset)
        self.invalidate_data()
    
    async def add_component(
        self,
        component_type : str,
        **members : Member
    ) -> ComponentProxy:
        component = await self.client.add_component(
            container_slot=self.id,
            component_type=component_type,
            **members
        )
        self.invalidate_data()
        return component
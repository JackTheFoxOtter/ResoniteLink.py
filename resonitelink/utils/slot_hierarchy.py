from resonitelink.models.datamodel import Slot
from typing import Any, List, Callable, Generator, Optional


__all__ = (
    'SlotHierarchy',
)


class SlotHierarchy():
    """
    Represents a slot hierarchy.
    This is a helper class used to provide an easily traversable tree structure for slot data.

    """
    _slot : Slot
    _parent : Optional['SlotHierarchy']
    _children : List['SlotHierarchy']

    @property
    def slot(self):
        return self._slot
    
    @property
    def parent(self):
        return self._parent
    
    @property
    def children(self):
        return self._children

    @property
    def children_count(self):
        return len(self.children)

    @property
    def children_count_recursive(self):
        return len(self.children) + sum([ child.children_count_recursive for child in self.children ])

    @property
    def component_count(self):
        return len(self.slot.components)

    @property
    def component_count_recursive(self):
        return len(self.slot.components) + sum([ child.component_count_recursive for child in self.children ])

    def __init__(self, slot : Slot, parent : Optional['SlotHierarchy'], children : List['SlotHierarchy']):
        self._slot = slot
        self._parent = parent
        self._children = children
    
    def __str__(self) -> str:
        return f"<SlotHierarchy: { '.'.join([ hierarchy.slot.name.value for hierarchy in self.get_path() ]) }>"
    
    def get_path(self) -> Generator['SlotHierarchy', Any, Any]:
        """
        Yields all parent `SlotHierarchies` leading up to the current hierarchy.

        Returns
        -------
        A generator yielding the `SlotHierarchy` instances of all parents leading up to the current hierarchy.

        """
        def _generate_recursively(hierarchy : 'SlotHierarchy') -> Generator['SlotHierarchy', Any, Any]:
            if hierarchy.parent:
                yield from _generate_recursively(hierarchy.parent)
            
            yield hierarchy
        
        yield from _generate_recursively(self)

    def find(self, search_expr : Callable[['SlotHierarchy'], bool], include_self : bool = True, search_depth : int = -1) -> Generator['SlotHierarchy', Any, Any]:
        """
        Searches the current hierarchy recursively and yields all `SlotHierarchy` instances matching the search expression.

        Parameters
        ----------
        search_expr : Callable[[SlotHierarchy], bool]
            The expression to invoke for each processed `SlotHierarchy` to determine wether it should get yielded or not.
        include_self : bool, default = True
            Wether to include the search root in the produced slot data. If `True`, the current `SlotHierarchy` will also be yielded, provided it passes the search expression.
        search_depth : int, default = -1
            Max recursive search depth. Children beyond this limit will not get processed. -1 for no infinite search depth.
        
        Returns
        -------
        Generator yielding all slots from the target hierarchy matching the search parameters.
        
        """
        def _generate_recursively(hierarchy : 'SlotHierarchy', depth : int) -> Generator['SlotHierarchy', Any, Any]:
            """
            Generator to recursively yield all hierarchies matching the search parameters.

            """
            if ( include_self or depth > 0 ) and search_expr(hierarchy):
                # Found a match! Yield it before processing potential children
                yield hierarchy
            
            if hierarchy.children and ( search_depth == -1 or depth < search_depth ):
                # Process children recursively
                for child_hierarchy in hierarchy.children:
                    yield from _generate_recursively(child_hierarchy, depth + 1)
        
        yield from _generate_recursively(self, 0)

    def format(
        self,
        line_format : Callable[['SlotHierarchy'], str] = lambda h: f"Slot '{h.slot.name.value}' ({len(h.slot.children) if h.children else 0} Child Slot(s), {len(h.slot.components) if h.slot.components else 0} Component(s))",
        expand_check : Callable[['SlotHierarchy'], bool] = lambda h: True
    ) -> str:
        """
        Utility function to recursively generate a nicely formatted string of a slot hierarchy.

        Parameters
        ----------
        line_format : Callable[[SlotHierarchy], str], optional
            Function to determine text to display for each `SlotHierarchy` (excluding prefix).
        expand_check : Callable[[SlotHierarchy], str], optional
            Function to determine wether to display each `SlotHierarchy` as 'expanded' (i.e. should child slots be resolved further).
        
        Returns
        -------
        Formatted multi-line string of specified slot hierarchy.

        """
        def _generate_recursively(hierarchy : 'SlotHierarchy', depth = 0, is_last : bool = False, prefixes : List[str] = []) -> Generator[str, Any, Any]:
            """
            Generator to recursively yield lines for multi-line string of specified slot hierarchy.

            """
            # Add line for slot
            if depth == 0:
                # Without prefix
                yield line_format(hierarchy)
            else:
                # With prefix
                yield f"{''.join(prefixes)}{' └─' if is_last else ' ├─'}{line_format(hierarchy)}"
            
            if hierarchy.children:
                # Determine prefixes for child
                child_prefixes : List[str]
                if depth == 0:
                    child_prefixes = prefixes
                else:
                    child_prefixes = prefixes + [ '   ' if is_last else ' │ ' ]

                if expand_check(hierarchy):
                    # Process children recursively
                    child_count = len(hierarchy.children)
                    for child_index, child_hierarchy in enumerate(hierarchy.children):
                        yield from _generate_recursively(child_hierarchy, depth + 1, child_index == child_count - 1, child_prefixes)
                
                else:
                    # Add indicator for left out child slots
                    yield f"{''.join(child_prefixes)} └─[...]"
        
        return "\n".join(_generate_recursively(self))

    @classmethod
    def from_slot(cls, slot : Slot) -> 'SlotHierarchy':
        """
        Constructs a `SlotHierarchy` instance from the provided `Slot` instance.
        Any child `Slot`s will be resolved recursively to their own `SlotHierarchy` instances.

        Note
        ----
        The produced hierarchy will **only** contain information about slots present in the input `Slot` instance.
        If you want to represent a full scene hierarchy, a fully resolved `Slot` instance is required.

        Parameters
        ----------
        slot : Slot
            The slot to create the hierarchy for.

        """
        def _from_slot(slot : Slot, parent_hierarchy : Optional['SlotHierarchy'] = None):
            """
            Recursively produces the `SlotHierarchy` instances.

            """
            hierarchy = cls(slot, parent_hierarchy, [])
            children = [ _from_slot(child_slot, hierarchy) for child_slot in slot.children ] if slot.children else [ ]
            hierarchy.children.extend(children)

            return hierarchy

        return _from_slot(slot, None)

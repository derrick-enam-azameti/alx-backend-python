#!/usr/bin/env python3
'''Task 1. Async Comprehensions
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Generate 10 random numbers using an async comprehensing
    '''
    return [num async for num in async_generator()]

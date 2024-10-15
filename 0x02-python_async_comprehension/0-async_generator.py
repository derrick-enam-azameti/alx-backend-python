#!/usr/bin/env python3
'''Task 0. Async Generator
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''Yield a random number between 0 and 10.
    Waiting 1 second each time.
    Loop 10 times.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

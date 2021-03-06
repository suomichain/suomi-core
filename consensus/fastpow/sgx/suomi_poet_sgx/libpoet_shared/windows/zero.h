/*
 Copyright 2017 Suomi Corporation

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
------------------------------------------------------------------------------
*/

#pragma once
#include <string.h>
#include <windows.h>
#include <vector>

template <typename T> inline void Zero(
    T& v
    )
{
    RtlSecureZeroMemory(&v, sizeof(T));
} // Zero

template <typename T> inline void ZeroV(
    std::vector<T>& v
    )
{
    RtlSecureZeroMemory(&v[0], sizeof(T));
} // ZeroV

inline void Zero(
    void* v,
    size_t length
    )
{
    RtlSecureZeroMemory(v, length);
} // Zero

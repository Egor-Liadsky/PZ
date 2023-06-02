package com.lydsky.dto

import kotlinx.serialization.Serializable

@Serializable
data class NoteDTOResponse(
    val id: Int,
    val title: String,
    val description: String,
    val date: String
)

@Serializable
data class NoteDTOReceive(
    val title: String,
    val description: String,
    val date: String
)
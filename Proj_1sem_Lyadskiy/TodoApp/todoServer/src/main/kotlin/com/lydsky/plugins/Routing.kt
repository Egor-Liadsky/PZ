package com.lydsky.plugins

import com.lydsky.features.notes.noteRouting
import io.ktor.server.routing.*
import io.ktor.server.response.*
import io.ktor.server.application.*

fun Application.configureRouting() {
    routing {
        route("/api/"){
            noteRouting()
        }
    }
}

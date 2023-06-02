package com.lydsky.features.notes

import com.lydsky.dto.NoteDTOReceive
import io.ktor.http.*
import io.ktor.server.application.*
import io.ktor.server.request.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import org.koin.ktor.ext.inject

fun Route.noteRouting() {

    val noteController by inject<NoteController>()

    get("/notes"){
        call.respond(noteController.getNotes())
    }

    post("/notes") {
        val noteReceive = call.receive<NoteDTOReceive>()
        noteController.createNote(noteReceive)
        call.respond(HttpStatusCode.Created, "Note created")
    }

    put ("/notes/{id}"){
        val noteReceive = call.receive<NoteDTOReceive>()
        val id = call.parameters["id"] ?: return@put call.respond(HttpStatusCode.NotFound, "Missing id")
        noteController.updateNote(id.toInt(), noteReceive)
        call.respond(HttpStatusCode.OK, "Note updated")
    }

    delete("/notes/{id}") {
        val id = call.parameters["id"] ?:  return@delete call.respond(HttpStatusCode.NotFound, "Missing id")
        noteController.deleteNote(id.toInt())
        call.respond(HttpStatusCode.OK, "Note deleted")
    }
}
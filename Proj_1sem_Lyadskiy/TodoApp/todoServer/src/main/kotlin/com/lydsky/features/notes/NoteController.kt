package com.lydsky.features.notes

import com.lydsky.database.dao.NoteDAO
import com.lydsky.dto.NoteDTOReceive
import com.lydsky.dto.NoteDTOResponse
import io.ktor.util.reflect.*

interface NoteController {
    suspend fun createNote(noteDTOReceive: NoteDTOReceive)
    suspend fun getNotes(): List<NoteDTOResponse>
    suspend fun updateNote(id: Int, noteDTOReceive: NoteDTOReceive)
    suspend fun deleteNote(id: Int)
}

class NoteControllerImpl(private val noteDAO: NoteDAO): NoteController {

    override suspend fun createNote(noteDTOReceive: NoteDTOReceive)  {
        noteDAO.createNote(noteDTOReceive)
    }

    override suspend fun getNotes(): List<NoteDTOResponse> {
        return noteDAO.getNotes()
    }

    override suspend fun updateNote(id: Int, noteDTOReceive: NoteDTOReceive) {
        noteDAO.updateNote(id, noteDTOReceive)
    }

    override suspend fun deleteNote(id: Int) {
        noteDAO.deleteNote(id)
    }
}
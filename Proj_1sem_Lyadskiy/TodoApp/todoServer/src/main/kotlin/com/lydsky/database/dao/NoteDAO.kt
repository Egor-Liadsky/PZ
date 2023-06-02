package com.lydsky.database.dao

import com.lydsky.database.DatabaseFactory.dbQuery
import com.lydsky.database.entity.NoteEntity
import com.lydsky.database.entity.NoteEntity.rowId
import com.lydsky.dto.NoteDTOReceive
import com.lydsky.dto.NoteDTOResponse
import org.jetbrains.exposed.sql.SqlExpressionBuilder.eq
import org.jetbrains.exposed.sql.deleteWhere
import org.jetbrains.exposed.sql.insert
import org.jetbrains.exposed.sql.selectAll
import org.jetbrains.exposed.sql.update

interface NoteDAO {
    suspend fun createNote(noteDTOReceive: NoteDTOReceive)
    suspend fun getNotes(): List<NoteDTOResponse>
    suspend fun updateNote(id : Int, noteDTOReceive: NoteDTOReceive)
    suspend fun deleteNote(id: Int)
}

class NoteDAOImpl : NoteDAO {

    override suspend fun createNote(noteDTOReceive: NoteDTOReceive) = dbQuery {
        NoteEntity.insert {
            it[title] = noteDTOReceive.title
            it[description] = noteDTOReceive.description
            it[date] = noteDTOReceive.date
        }
        return@dbQuery
    }

    override suspend fun getNotes(): List<NoteDTOResponse> = dbQuery {
        val noteEntity = NoteEntity.selectAll().map {
            NoteDTOResponse(
                id = it[NoteEntity.rowId],
                title = it[NoteEntity.title],
                description = it[NoteEntity.description],
                date = it[NoteEntity.date]
            )
        }
        return@dbQuery noteEntity
    }

    override suspend fun updateNote(id : Int, noteDTOReceive: NoteDTOReceive) = dbQuery{
        NoteEntity.update({rowId eq id}){
            it[NoteEntity.title] = noteDTOReceive.title
            it[NoteEntity.description] = noteDTOReceive.description
            it[NoteEntity.date] = noteDTOReceive.date
        }
        return@dbQuery
    }

    override suspend fun deleteNote(id: Int) = dbQuery{
        NoteEntity.deleteWhere { rowId eq id }
        return@dbQuery
    }
}
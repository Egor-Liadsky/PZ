package com.lydsky.database.entity

import org.jetbrains.exposed.sql.Table


object NoteEntity : Table("notes") {
    val rowId = integer("id").autoIncrement()
    val title = varchar("title", 200)
    val description = varchar("description", 1000)
    val date = varchar("date", 45)

    override val primaryKey = PrimaryKey(rowId, name = "id")
}
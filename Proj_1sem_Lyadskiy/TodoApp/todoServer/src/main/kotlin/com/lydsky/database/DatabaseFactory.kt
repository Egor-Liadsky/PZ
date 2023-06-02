package com.lydsky.database

import com.lydsky.database.entity.NoteEntity
import com.lydsky.utils.Constants
import org.jetbrains.exposed.sql.Database
import org.jetbrains.exposed.sql.SchemaUtils
import org.jetbrains.exposed.sql.StdOutSqlLogger
import org.jetbrains.exposed.sql.addLogger
import org.jetbrains.exposed.sql.transactions.experimental.newSuspendedTransaction
import org.jetbrains.exposed.sql.transactions.transaction


object DatabaseFactory {

    fun init(){
        val driver = "com.mysql.cj.jdbc.Driver"
        val jdbcUrl = "jdbc:mysql://localhost:3306/${Constants.DATABASE_NAME}?useSSL=false"
        Database.connect(jdbcUrl, driver = driver,user = Constants.USER_DATABASE, password = Constants.PASSWORD_DATABASE)

        transaction {
            addLogger(StdOutSqlLogger)
            SchemaUtils.create(NoteEntity)
        }
    }

    suspend fun <T> dbQuery(block: suspend () -> T): T =
        newSuspendedTransaction { block() }
}
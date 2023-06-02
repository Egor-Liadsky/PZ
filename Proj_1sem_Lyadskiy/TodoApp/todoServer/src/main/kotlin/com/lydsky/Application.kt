package com.lydsky

import com.lydsky.database.DatabaseFactory
import io.ktor.server.application.*
import com.lydsky.plugins.*

fun main(args: Array<String>): Unit =
    io.ktor.server.netty.EngineMain.main(args)

@Suppress("unused")
fun Application.module() {
    configureKoin()
    configureSerialization()
    configureRouting()

    DatabaseFactory.init()
}

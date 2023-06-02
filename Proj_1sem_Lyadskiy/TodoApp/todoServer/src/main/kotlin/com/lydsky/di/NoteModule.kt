package com.lydsky.di

import com.lydsky.database.dao.NoteDAO
import com.lydsky.database.dao.NoteDAOImpl
import com.lydsky.features.notes.NoteController
import com.lydsky.features.notes.NoteControllerImpl
import org.koin.dsl.module

val noteModule = module {
    single<NoteDAO> { NoteDAOImpl() }
    single<NoteController> { NoteControllerImpl(get()) }
}
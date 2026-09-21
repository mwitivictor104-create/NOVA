package com.nova.bubble.chat

import com.nova.bubble.TermuxBridge

class ChatManager {

    interface ChatListener {
        fun onReply(reply: String)
    }

    private var listener: ChatListener? = null

    fun setListener(chatListener: ChatListener) {
        listener = chatListener
    }

    fun sendMessage(message: String) {

        if (message.isBlank()) return

        TermuxBridge.send(message) { reply ->
            listener?.onReply(reply)
        }
    }
}

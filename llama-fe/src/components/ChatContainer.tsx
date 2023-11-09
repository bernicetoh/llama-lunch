import React, { useEffect, useRef, useState } from "react";
import ChatBubble from "./ChatBubble";
import { Message } from "../utils";
import Loader from "./Loader";
import llama from "../assets/llama.png";

interface Props {
  messages: Message[];
  msg: string | null;
  reply: string | null;
  isFetching: boolean;
}
function ChatContainer({ messages, msg, reply, isFetching }: Props) {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    ref.current?.scrollIntoView({ behavior: "smooth", block: "end" });
  }, [messages, msg, reply, isFetching]);

  return (
    <div className="flex flex-1 p-5 overflow-y-auto flex-col">
      {messages.length > 0 ? (
        <div className="flex flex-col flex-1">
          {messages.map((m, index) => (
            <ChatBubble key={index} text={m.message} isUser={m.isUser} />
          ))}
          {isFetching && (
            <div className="flex gap-[10px]">
              <div className="rounded-lg w-11 h-11 p-2 bg-orange-50">
                <img className="" alt="llama" src={llama} />
              </div>
              <div className="w-[150px]flex bg-orange-50 self-start text-clip p-5 mb-5 rounded-lg whitespace-pre-line">
                <Loader />
              </div>
            </div>
          )}
          <div ref={ref} />
        </div>
      ) : (
        <div className="flex flex-1 items-center justify-center text-lg flex-col gap-10 text-slate-400">
          Enter ingredients and let LlaMa Lunch generate a recipe for you!
          <img
            src={llama}
            alt="llama"
            className="w-[300px] drop-shadow-[0, 0, 0, blue] opacity-[0.1]"
          />
        </div>
      )}
    </div>
  );
}

export default ChatContainer;

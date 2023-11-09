import React from "react";
import llama from "../assets/llama.png";
interface Props {
  text: string;
  isUser: boolean;
  ref?: HTMLDivElement;
}
function ChatBubble({ text, isUser, ref }: Props) {
  return (
    <div className={`flex gap-[10px] ${isUser ? "self-end" : "self-start"}`}>
      {!isUser && (
        <div className="rounded-lg w-12 h-12 p-2 bg-orange-50">
          <img alt="llama" src={llama} />
        </div>
      )}
      <div
        className={`${
          isUser ? "bg-blue-50 self-end" : "bg-orange-50 self-start"
        } text-clip p-5 mb-5 rounded-lg whitespace-pre-line max-w-xl`}
      >
        {text}
      </div>
    </div>
  );
}

export default ChatBubble;

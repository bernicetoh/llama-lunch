import React, {
  Dispatch,
  SetStateAction,
  SyntheticEvent,
  useState,
} from "react";
import cook from "../assets/cook.png";
import axios from "axios";
import { VscDebugRestart } from "react-icons/vsc";
import { Message, saveMessages } from "../utils";
interface Props {
  setIsSent: Dispatch<SetStateAction<boolean>>;
  setCurrMsg: Dispatch<SetStateAction<string | null>>;
  currMsg: string | null;
  setRefetch: Dispatch<SetStateAction<boolean>>;
  setMessages: Dispatch<SetStateAction<Message[]>>;
  messages: Message[];
}
function TextInput({
  setCurrMsg,
  setIsSent,
  currMsg,
  setRefetch,
  setMessages,
  messages,
}: Props) {
  const [thisMsg, setThisMsg] = useState("");
  const clear = () => {
    setRefetch(true);
    localStorage.removeItem("messages");
    console.log("cleared!");
  };

  const handleSubmit = (e: SyntheticEvent) => {
    e.preventDefault();
    console.log("handling");
    setCurrMsg(thisMsg);
    const temp = messages;
    temp.push({ isUser: true, message: thisMsg });
    saveMessages(temp);
    setMessages(temp);
    setIsSent(true);
    setThisMsg("");
  };

  return (
    <div className="w-full flex pt-5">
      <form
        className="w-full flex justify-between gap-[15px]"
        onSubmit={handleSubmit}
      >
        <input
          className="flex flex-1 p-3 bg-slate-100 rounded-lg outline-black"
          placeholder="Enter ingredients"
          value={thisMsg}
          onChange={(e) => setThisMsg(e.target.value)}
        />
        <button
          className={`rounded-full p-2 w-[50px] h-[50px] 
          ${
            thisMsg.length === 0
              ? "bg-slate-400"
              : "bg-black hover:bg-slate-600 transition duration-200"
          }`}
          disabled={thisMsg.length === 0}
          type="submit"
        >
          <img src={cook} className="brightness-0 invert" alt="cook" />
        </button>
        <button
          type="button"
          onClick={clear}
          className="bg-black rounded-full p-2 w-[50px] h-[50px] flex items-center justify-center hover:bg-slate-600 transition duration-200"
        >
          <VscDebugRestart color="white" />
        </button>
      </form>
    </div>
  );
}

export default TextInput;

import React, { SyntheticEvent, useEffect, useState } from "react";
import cook from "./assets/cook.png";
import "./App.css";
import TextInput from "./components/TextInput";
import ChatContainer from "./components/ChatContainer";
import { Message, getRecipe, getReplyFromQn, saveMessages } from "./utils";
function App() {
  const [isSent, setIsSent] = useState(false);
  const [currMsg, setCurrMsg] = useState<string | null>(null);
  const [reply, setReply] = useState<string | null>(null);
  const [messages, setMessages] = useState<Message[]>([]);
  const [refetch, setRefetch] = useState(false);
  const [isFetching, setFetching] = useState(false);

  useEffect(() => {
    // load in messages from db
    const localMsgsString = localStorage.getItem("messages");
    let loadedMsgs = [];
    if (localMsgsString) {
      loadedMsgs = JSON.parse(localMsgsString);
    }
    setMessages(loadedMsgs);
  }, []);

  useEffect(() => {
    const send = async () => {
      try {
        if (isSent) {
          console.log("fetching");
          setFetching(true);
          if (currMsg) {
            const res = await getReplyFromQn(currMsg);
            const temp = messages;
            temp.push({
              isUser: false,
              message: res,
            });
            saveMessages(temp);
            setMessages(temp);
            setFetching(false);
          }
        }
        setIsSent(false);
      } catch (e) {
        console.log(e);
      }
    };
    send();
  }, [isSent]);

  useEffect(() => {
    if (refetch) {
      setMessages([]);
      setCurrMsg(null);
      setReply(null);
      setRefetch(false);
    }
  }, [refetch]);

  return (
    <div className="w-screen h-screen flex justify-center">
      <div className="pt-3 pb-3 pl-6 pr-6 w-full h-full flex flex-col">
        <div className="flex items-center gap-[10px]">
          <div className="text-xl font-bold h-[40px] items-center flex">
            LlaMa Lunch
          </div>
          <img src={cook} alt="cook" className="w-[40px]" />
        </div>
        {/* chat container */}
        <ChatContainer
          reply={reply}
          msg={currMsg}
          messages={messages}
          isFetching={isFetching}
        />

        {/* text input */}
        <TextInput
          setRefetch={setRefetch}
          setIsSent={setIsSent}
          setCurrMsg={setCurrMsg}
          currMsg={currMsg}
          setMessages={setMessages}
          messages={messages}
        />
        {/* footer */}
        <div className="p-3 text-sm text-slate-500">
          Made with{" "}
          <a
            href="https://ai.meta.com/llama/"
            className="font-semibold"
            target="_blank"
            rel="noreferrer"
          >
            Llama2
          </a>
          , by Andre Lin, Bernice Toh, Kang Yue Ran
        </div>
      </div>
    </div>
  );
}

export default App;

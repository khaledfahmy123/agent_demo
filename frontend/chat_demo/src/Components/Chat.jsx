import styles from "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  ConversationHeader,
  Avatar,
  Sidebar,
  ExpansionPanel,
} from "@chatscope/chat-ui-kit-react";
import { useChat } from "./useChatHook";

const Chat = ({ connected }) => {
  const [messages, sendMessage, wait, sources] = useChat();

  const send = (msg) => {
    sendMessage(msg);
  };
  return (
    <div
      style={{
        position: "relative",
        height: "100vh",
        maxWidth: "1400px",
        margin: "auto",
        padding: "12px",
        boxSizing: "border-box",
      }}
    >
      <MainContainer>
        <ChatContainer>
          <ConversationHeader>
            <ConversationHeader.Back />
            <Avatar
              name="cBioPortal"
              src="https://docs.cbioportal.org/images/cbio-logo.png"
            />
            <ConversationHeader.Content
              info={connected ? "Connected" : "there is a connection problem!"}
              userName="cBioPortal"
            />
            <ConversationHeader.Actions></ConversationHeader.Actions>
          </ConversationHeader>
          <MessageList style={{ padding: "10px" }}>
            {messages.map((e) => (
              <Message model={e} />
            ))}
          </MessageList>
          <MessageInput
            placeholder="Type message here"
            onSend={send}
            sendDisabled={wait}
          />
        </ChatContainer>
        <Sidebar position="right">
          <ExpansionPanel open title="Sources" boxSizing="border-box">
            <ul
              padding="2px"
              style={{ padding: "7xp", margin: "0", wordWrap: "break-word" }}
              margin="0px"
            >
              {sources.map((e) => (
                <li>
                  <a href={e} target="__blank">
                    {e}
                  </a>
                </li>
              ))}
            </ul>
          </ExpansionPanel>
        </Sidebar>
      </MainContainer>
    </div>
  );
};

export default Chat;

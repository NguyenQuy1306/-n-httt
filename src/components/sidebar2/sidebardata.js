import React from "react";
import * as FaIcons from "react-icons/fa";
import * as AiIcons from "react-icons/ai";
import * as IoIcons from "react-icons/io";
import * as RiIcons from "react-icons/ri";
import { useState } from "react";

export const SidebarData = [
  {
    title: "Overview",
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
    path: "/Homepage",
  },
  {
    title: "Goal",
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
    path: "/goal",
  },
  {
    title: "Profile",
    icon: <AiIcons.AiFillHome />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
    path: "/profile",
  },
  {
    title: "Projects",
    icon: <IoIcons.IoIosPaper />,
    iconClosed: <RiIcons.RiArrowDownSFill />,
    iconOpened: <RiIcons.RiArrowUpSFill />,
    subNav: [
      {
        title: "Project 1",
        icon: <IoIcons.IoIosPaper />,
        iconClosed: <RiIcons.RiArrowDownSFill />,
        iconOpened: <RiIcons.RiArrowUpSFill />,
        path: "/project1",
        subsubNav: [
          {
            title: "Section 1",
            path: "/project1/section_1",
            icon: <IoIcons.IoIosPaper />,
          },
          {
            title: "Section 2",
            path: "/project1/section_2",
            icon: <IoIcons.IoIosPaper />,
          },
        ],
      },
      {
        title: "Project 2",
        icon: <IoIcons.IoIosPaper />,
        iconClosed: <RiIcons.RiArrowDownSFill />,
        iconOpened: <RiIcons.RiArrowUpSFill />,
        path: "/project2",
        subsubNav: [
          {
            title: "Section 1",
            // path: "/messages/message1/submessage1",
            icon: <IoIcons.IoIosPaper />,
          },
          {
            title: "Section 2",
            // path: "/messages/message1/submessage2",
            icon: <IoIcons.IoIosPaper />,
          },
        ],
      },
      // other subNav items...
    ],
  },
  {
    title: "Team",
    // path: "/team",
    icon: <IoIcons.IoMdPeople />,
  },
  {
    title: "Support",
    // path: "/support",
    icon: <IoIcons.IoMdHelpCircle />,
  },
];
localStorage.setItem("mySidebarData", JSON.stringify(SidebarData));

//
//  Shell.swift
//  
//
//  Created by Shota Shimazu on 2022/11/26.
//

import Foundation

@discardableResult
func shell(_ args: String) -> Int32 {
    let task = Process()
    task.launchPath = "/usr/bin/env"
    task.arguments = args.components(separatedBy: " ")
    task.launch()
    task.waitUntilExit()
    return task.terminationStatus
}
